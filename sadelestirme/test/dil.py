# -*- coding: utf-8 -*-
"""QueenStocks formul dili icin kucuk yorumlayici (Python float = IEEE double).

Formul METNINI dogrudan ayristirir (elle kopyalama hatasi olmasin diye).
Anlam modeli (null, sifira bolme, and/or, atama donusumu) parametreli.
"""
import math, re, struct

class Hata(Exception):
    pass

# ---------------- veri cagrisi -> girdi alani eslemesi ----------------
def _k(name, args):
    return (name, tuple(args))

CAGRI = {
    _k('OzsermayeKarlilikYillik', []): 'ROE0',
    _k('OzsermayeKarlilikYillik', ['', -1.0]): 'ROE1',
    _k('OzsermayeKarlilikYillik', ['', -4.0]): 'ROE4',
    _k('FAVOKYillik', []): 'FAVOKY',
    _k('NetBorc', []): 'NETBORC',
    _k('PDDD', []): 'PDDD',
    _k('NetKarYillik', []): 'NKY',
    _k('PD', []): 'PD',
    _k('Getiri', ['s2a', 'TL']): 'G2a',
    _k('Getiri', ['s2a', 'TL', 'XUTUM']): 'G2aX',
    _k('Getiri', ['s1a', 'TL']): 'G1a',
    _k('Getiri', ['s12a', 'TL']): 'G12a',
    _k('Getiri', ['s2h', 'TL']): 'G2h',
    _k('Getiri', ['s2h', 'TL', 'XUTUM']): 'G2hX',
    _k('HAOran', []): 'HA',
    _k('NetSatisBuyumeYillik', []): 'SATISB',
    _k('Tufe', [12.0]): 'TUFE',
    _k('FAVOKBuyumeYillik', []): 'FAVOKB',
    _k('FAVOK', ['TL', 0.0]): 'F0',
    _k('FAVOK', ['TL', -1.0]): 'F1',
    _k('FAVOK', ['TL', -4.0]): 'F4',
    _k('BrutEFKBuyumeYillik', []): 'BRUTB',
    _k('BrutEFK', ['TL', 0.0]): 'B0',
    _k('BrutEFK', ['TL', -1.0]): 'B1',
    _k('BrutEFK', ['TL', -4.0]): 'B4',
    _k('EFKBuyumeYillik', []): 'EFKB',
    _k('EFKBuyumeYillik', ['', -1.0]): 'EFKB1',
    _k('EFK', ['TL', 0.0]): 'E0',
    _k('EFK', ['TL', -1.0]): 'E1',
    _k('EFK', ['TL', -4.0]): 'E4',
    _k('Teknik.Indicator', ['C/HHV(H,252)', 'd']): 'Z',
    _k('Teknik.Indicator', ['C/Mov(C,75,S)', 'd']): 'R75',
    _k('Teknik.Indicator', ['Ref(C,-21)/Ref(C,-126)', 'd']): 'M6',
    # Teknik kutusu (MetaStock benzeri)
    _k('Mov', ['@C', 200.0]): 'MA200',
    _k('Mov', ['@C', 75.0]): 'MA75',
    _k('Mov', ['@C', 20.0]): 'MA20',
    _k('Mov', ['@C', 60.0]): 'MA60',
}
ALANLAR = ['ROE0', 'ROE1', 'ROE4', 'FAVOKY', 'NETBORC', 'PDDD', 'NKY', 'PD', 'G2a', 'G2aX', 'G1a', 'HA',
           'G12a', 'G2h', 'G2hX', 'SATISB', 'TUFE', 'FAVOKB', 'F0', 'F1', 'F4', 'BRUTB', 'B0', 'B1', 'B4',
           'EFKB', 'EFKB1', 'E0', 'E1', 'E4', 'Z', 'R75', 'M6', 'C', 'MA200', 'MA75', 'MA20', 'MA60']

# ---------------- tokenizer + parser ----------------
TOK = re.compile(r'\s*(?:(\d+\.\d*|\d*\.\d+|\d+)|("[^"]*")|([A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)?)|(>=|<=|==|!=|[-+*/()<>,;=]))')

def tokenize(src):
    # '//' yorumlarini satir sonuna kadar sil
    lines = []
    for ln in src.splitlines():
        i = ln.find('//')
        lines.append(ln if i < 0 else ln[:i])
    s = '\n'.join(lines)
    pos, out = 0, []
    s = s.rstrip()
    while pos < len(s):
        m = TOK.match(s, pos)
        if not m or m.end() == pos:
            if s[pos:].strip() == '':
                break
            raise SyntaxError('tok @%d: %r' % (pos, s[pos:pos + 20]))
        pos = m.end()
        num, st, ident, op = m.groups()
        if num is not None:
            out.append(('num', float(num)))
        elif st is not None:
            out.append(('str', st[1:-1]))
        elif ident is not None:
            if ident in ('and', 'or'):
                out.append(('op', ident))
            elif ident == 'null':
                out.append(('null', None))
            else:
                out.append(('id', ident))
        else:
            out.append(('op', op))
    return out

class P:
    def __init__(self, toks):
        self.t = toks; self.i = 0
    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else ('eof', None)
    def eat(self, v=None):
        tk = self.peek()
        if v is not None and tk[1] != v:
            raise SyntaxError('beklenen %r, gelen %r @%d' % (v, tk, self.i))
        self.i += 1
        return tk
    def program(self):
        stmts = []
        while self.peek()[0] != 'eof':
            # atama mi?
            tk = self.peek()
            if tk[0] == 'id' and self.i + 1 < len(self.t) and self.t[self.i + 1] == ('op', '='):
                name = self.eat()[1]; self.eat('=')
                e = self.expr()
                stmts.append(('asg', name, e))
            else:
                stmts.append(('expr', self.expr()))
            self.eat(';')
        return stmts
    def expr(self):
        return self.orx()
    def orx(self):
        items = [self.andx()]
        while self.peek() == ('op', 'or'):
            self.eat(); items.append(self.andx())
        return items[0] if len(items) == 1 else ('or', items)
    def andx(self):
        items = [self.cmp()]
        while self.peek() == ('op', 'and'):
            self.eat(); items.append(self.cmp())
        return items[0] if len(items) == 1 else ('and', items)
    def cmp(self):
        l = self.add()
        tk = self.peek()
        if tk[0] == 'op' and tk[1] in ('>', '<', '>=', '<=', '==', '!='):
            self.eat(); r = self.add()
            return ('cmp', tk[1], l, r)
        return l
    def add(self):
        l = self.mul()
        while self.peek()[0] == 'op' and self.peek()[1] in '+-' and len(self.peek()[1]) == 1:
            op = self.eat()[1]; r = self.mul(); l = ('bin', op, l, r)
        return l
    def mul(self):
        l = self.un()
        while self.peek()[0] == 'op' and self.peek()[1] in ('*', '/'):
            op = self.eat()[1]; r = self.un(); l = ('bin', op, l, r)
        return l
    def un(self):
        if self.peek() == ('op', '-'):
            self.eat(); x = self.un()
            if x[0] == 'num':
                return ('num', -x[1])        # sabit: -15, -1, -4
            return ('neg', x)
        return self.atom()
    def atom(self):
        tk = self.eat()
        if tk[0] == 'num':
            return ('num', tk[1])
        if tk[0] == 'str':
            return ('str', tk[1])
        if tk[0] == 'null':
            return ('null',)
        if tk == ('op', '('):
            e = self.expr(); self.eat(')'); return e
        if tk[0] == 'id':
            if self.peek() == ('op', '('):
                self.eat()
                args = []
                if self.peek() != ('op', ')'):
                    args.append(self.expr())
                    while self.peek() == ('op', ','):
                        self.eat(); args.append(self.expr())
                self.eat(')')
                return ('call', tk[1], args)
            return ('var', tk[1])
        raise SyntaxError('atom %r' % (tk,))

def parse(src):
    return P(tokenize(src)).program()

# ---------------- anlam modeli ----------------
INF = float('inf'); NAN = float('nan')

def ieee_div(a, b):
    if b == 0.0:
        if a == 0.0 or a != a:
            return NAN
        return math.copysign(INF, a) * math.copysign(1.0, b)
    return a / b

class Model:
    """null: 'G3' (M1) | 'YAY' (M2)
       bolme: 'null' | 'ieee' | 'hata'
       mantik: 'hevesli' | 'kisa'
       atama: 'yok' | 'nan2null' | 'sonsuz2null' | 'null2sifir'"""
    def __init__(self, null='G3', bolme='null', mantik='kisa', atama='yok'):
        self.null, self.bolme, self.mantik, self.atama = null, bolme, mantik, atama
        self.ad = '%s/%s/%s/%s' % (null, bolme, mantik, atama)

    def asg(self, v):
        a = self.atama
        if a == 'yok':
            return v
        if a == 'nan2null':
            return None if (isinstance(v, float) and v != v) else v
        if a == 'sonsuz2null':
            return None if (isinstance(v, float) and not math.isfinite(v)) else v
        if a == 'null2sifir':
            return 0.0 if v is None else v
        # Ara sonuclar tabloya/sutuna yazilip okunuyorsa (ifade bazli backtest) hassasiyet kaybi:
        if a == 'float32':
            if not isinstance(v, float) or not math.isfinite(v):
                return v
            if abs(v) > 3.4028234663852886e38:
                return math.copysign(INF, v)
            return struct.unpack('f', struct.pack('f', v))[0]
        if a.startswith('yuvarla'):      # yuvarla4, yuvarla6: decimal(.,4/6) saklama
            if not isinstance(v, float) or not math.isfinite(v):
                return v
            if abs(v) > 1e15:
                return v
            return round(v, int(a[7:]))
        raise ValueError(a)

    def arith(self, op, a, b):
        if a is None or b is None:
            if self.null == 'YAY':
                return None
            a = 0.0 if a is None else a
            b = 0.0 if b is None else b
        if a is True or a is False or b is True or b is False:
            raise Hata('boolean aritmetikte')
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if b == 0.0:
            if self.bolme == 'null': return None
            if self.bolme == 'hata': raise Hata('sifira bolme')
            return ieee_div(a, b)
        return a / b

    def absf(self, a):
        if a is None:
            return None if self.null == 'YAY' else 0.0
        return abs(a)

    def cmp(self, op, a, b):
        if a is None or b is None:
            return False
        if op == '>': return a > b
        if op == '<': return a < b
        if op == '>=': return a >= b
        if op == '<=': return a <= b
        if op == '==': return a == b
        if op == '!=': return a != b

# ---------------- derleyici (AST -> Python closure) ----------------
def compile_prog(stmts, M, sayac=None):
    """Donus: f(veri) -> son ifadenin degeri (Hata firlatabilir), ve degisken izi."""
    def ce(n):
        k = n[0]
        if k == 'num':
            v = n[1]; return lambda d, env: v
        if k == 'null':
            return lambda d, env: None
        if k == 'var':
            nm = n[1]
            if nm in ('C',):
                return lambda d, env: (env[nm] if nm in env else d['C'])
            def fv(d, env, nm=nm):
                if nm not in env:
                    raise KeyError('tanimsiz degisken ' + nm)
                return env[nm]
            return fv
        if k == 'neg':
            x = ce(n[1]); return lambda d, env: M.arith('-', 0.0, x(d, env))
        if k == 'bin':
            op = n[1]; l = ce(n[2]); r = ce(n[3])
            return lambda d, env: M.arith(op, l(d, env), r(d, env))
        if k == 'cmp':
            op = n[1]
            if n[3][0] == 'null' and op == '==':
                l = ce(n[2]); return lambda d, env: (l(d, env) is None)
            l = ce(n[2]); r = ce(n[3])
            return lambda d, env: M.cmp(op, l(d, env), r(d, env))
        if k in ('and', 'or'):
            fs = [ce(x) for x in n[1]]
            isand = (k == 'and')
            if M.mantik == 'kisa':
                if isand:
                    def f(d, env):
                        for g in fs:
                            if g(d, env) is not True:
                                return False
                        return True
                else:
                    def f(d, env):
                        for g in fs:
                            if g(d, env) is True:
                                return True
                        return False
            else:
                if isand:
                    def f(d, env):
                        vs = [g(d, env) for g in fs]
                        return all(v is True for v in vs)
                else:
                    def f(d, env):
                        vs = [g(d, env) for g in fs]
                        return any(v is True for v in vs)
            return f
        if k == 'call':
            nm, args = n[1], n[2]
            if nm == 'IF':
                c, a, b = [ce(x) for x in args]
                def fif(d, env):
                    cv = c(d, env); av = a(d, env); bv = b(d, env)   # hevesli: iki kol da hesaplanir
                    return av if cv is True else bv
                return fif
            if nm == 'Abs':
                x = ce(args[0]); return lambda d, env: M.absf(x(d, env))
            key = []
            for a in args:
                if a[0] in ('num', 'str'):
                    key.append(a[1])
                elif a == ('var', 'C'):
                    key.append('@C')
                else:
                    raise SyntaxError('veri cagrisinda sabit olmayan arguman: %r' % (a,))
            alan = CAGRI.get((nm, tuple(key)))
            if alan is None:
                raise SyntaxError('bilinmeyen cagri %s%r' % (nm, key))
            if sayac is not None:
                sayac.append(alan)
            return lambda d, env, alan=alan: d[alan]
        raise SyntaxError('dugum %r' % (k,))

    comp = []
    for s in stmts:
        if s[0] == 'asg':
            comp.append((s[1], ce(s[2])))
        else:
            comp.append((None, ce(s[1])))
    if comp[-1][0] is not None:
        raise SyntaxError('son ifade atama olmamali')

    def run(d, iz=None):
        env = {}
        v = None
        for name, f in comp:
            v = f(d, env)
            if name is not None:
                env[name] = M.asg(v)
        if iz is not None:
            iz.update(env)
        return M.asg(v)   # sonuc da ayni donusumden gecer (iki surume de esit uygulanir)
    return run
