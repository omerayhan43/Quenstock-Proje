# -*- coding: utf-8 -*-
"""Deger (BISTTUM) formulleri icin genellestirilmis yorumlayici. Buyume'deki dil.py'den turetildi.
Eklenenler: '||' (her zaman kisa devre), AND/OR buyuk harf, null argumanli cagrilar, Log, YilEkle,
AnalizTarih, son ifadenin atama olabilmesi, veri cagrilarinin otomatik alan eslemesi."""
import math, re, struct, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test'))
from dil import Model, Hata, ieee_div

TOK = re.compile(r'\s*(?:(\d+\.\d*|\d*\.\d+|\d+)|("[^"]*")|([A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)?)|(\|\||>=|<=|==|!=|[-+*/()<>,;=]))')

def tokenize(src):
    s = '\n'.join(ln if ln.find('//') < 0 else ln[:ln.find('//')] for ln in src.splitlines()).rstrip()
    pos, out = 0, []
    while pos < len(s):
        m = TOK.match(s, pos)
        if not m or m.end() == pos:
            if s[pos:].strip() == '': break
            raise SyntaxError('tok @%d %r' % (pos, s[pos:pos+20]))
        pos = m.end()
        num, st, ident, op = m.groups()
        if num is not None: out.append(('num', float(num)))
        elif st is not None: out.append(('str', st[1:-1]))
        elif ident is not None:
            if ident.lower() in ('and', 'or'): out.append(('op', ident.lower()))
            elif ident == 'null': out.append(('null', None))
            else: out.append(('id', ident))
        else: out.append(('op', op))
    return out

class P:
    def __init__(s, t): s.t, s.i = t, 0
    def peek(s): return s.t[s.i] if s.i < len(s.t) else ('eof', None)
    def eat(s, v=None):
        tk = s.peek()
        if v is not None and tk[1] != v: raise SyntaxError('beklenen %r gelen %r' % (v, tk))
        s.i += 1; return tk
    def program(s):
        st = []
        while s.peek()[0] != 'eof':
            tk = s.peek()
            if tk[0] == 'id' and s.i+1 < len(s.t) and s.t[s.i+1] == ('op', '='):
                n = s.eat()[1]; s.eat('='); st.append(('asg', n, s.expr()))
            else: st.append(('expr', s.expr()))
            s.eat(';')
        return st
    def expr(s): return s.orx()
    def orx(s):
        items = [s.andx()]; kind = None
        while s.peek() in (('op', 'or'), ('op', '||')):
            k = 'oror' if s.eat()[1] == '||' else 'or'
            if kind and kind != k: raise SyntaxError('or ve || karisik')
            kind = k; items.append(s.andx())
        return items[0] if len(items) == 1 else (kind, items)
    def andx(s):
        items = [s.cmp()]
        while s.peek() == ('op', 'and'): s.eat(); items.append(s.cmp())
        return items[0] if len(items) == 1 else ('and', items)
    def cmp(s):
        l = s.add(); tk = s.peek()
        if tk[0] == 'op' and tk[1] in ('>', '<', '>=', '<=', '==', '!='):
            s.eat(); return ('cmp', tk[1], l, s.add())
        return l
    def add(s):
        l = s.mul()
        while s.peek()[0] == 'op' and s.peek()[1] in ('+', '-'):
            op = s.eat()[1]; l = ('bin', op, l, s.mul())
        return l
    def mul(s):
        l = s.un()
        while s.peek()[0] == 'op' and s.peek()[1] in ('*', '/'):
            op = s.eat()[1]; l = ('bin', op, l, s.un())
        return l
    def un(s):
        if s.peek() == ('op', '-'):
            s.eat(); x = s.un()
            return ('num', -x[1]) if x[0] == 'num' else ('neg', x)
        return s.atom()
    def atom(s):
        tk = s.eat()
        if tk[0] == 'num': return ('num', tk[1])
        if tk[0] == 'str': return ('str', tk[1])
        if tk[0] == 'null': return ('null',)
        if tk == ('op', '('):
            e = s.expr(); s.eat(')'); return e
        if tk[0] == 'id':
            if s.peek() == ('op', '('):
                s.eat(); args = []
                if s.peek() != ('op', ')'):
                    args.append(s.expr())
                    while s.peek() == ('op', ','): s.eat(); args.append(s.expr())
                s.eat(')'); return ('call', tk[1], args)
            return ('var', tk[1])
        raise SyntaxError('atom %r' % (tk,))

def parse(src): return P(tokenize(src)).program()

def alan_adi(nm, args):
    parts = []
    for a in args:
        if a[0] == 'num': parts.append(repr(a[1]))
        elif a[0] == 'str': parts.append(a[1])
        elif a[0] == 'null': parts.append('null')
        elif a == ('var', 'C'): parts.append('C')
        else: return None
    return nm + '(' + ','.join(parts) + ')'

VERI_DEGISKEN = {'AnalizTarih'}

def compile_prog(stmts, M, alanlar=None):
    def ce(n):
        k = n[0]
        if k == 'num': v = n[1]; return lambda d, e: v
        if k == 'null': return lambda d, e: None
        if k == 'var':
            nm = n[1]
            if nm in VERI_DEGISKEN:
                if alanlar is not None: alanlar.add(nm)
                return lambda d, e: d[nm]
            def fv(d, e, nm=nm):
                if nm not in e: raise KeyError('tanimsiz ' + nm)
                return e[nm]
            return fv
        if k == 'neg': x = ce(n[1]); return lambda d, e: M.arith('-', 0.0, x(d, e))
        if k == 'bin':
            op, l, r = n[1], ce(n[2]), ce(n[3]); return lambda d, e: M.arith(op, l(d, e), r(d, e))
        if k == 'cmp':
            op = n[1]
            if n[3][0] == 'null' and op == '==':
                l = ce(n[2]); return lambda d, e: l(d, e) is None
            l, r = ce(n[2]), ce(n[3]); return lambda d, e: M.cmp(op, l(d, e), r(d, e))
        if k == 'oror':
            fs = [ce(x) for x in n[1]]
            def f(d, e):
                for g in fs:
                    if g(d, e) is True: return True
                return False
            return f
        if k in ('and', 'or'):
            fs = [ce(x) for x in n[1]]; isand = k == 'and'
            if M.mantik == 'kisa':
                def f(d, e):
                    for g in fs:
                        v = g(d, e) is True
                        if isand and not v: return False
                        if not isand and v: return True
                    return isand
            else:
                def f(d, e):
                    vs = [g(d, e) is True for g in fs]
                    return all(vs) if isand else any(vs)
            return f
        if k == 'call':
            nm, args = n[1], n[2]
            if nm == 'IF':
                c, a, b = [ce(x) for x in args]
                def fif(d, e):
                    cv = c(d, e); av = a(d, e); bv = b(d, e)
                    if cv is not True and cv is not False:
                        if isinstance(cv, float): cv = cv != 0
                        else: cv = False
                    return av if cv else bv
                return fif
            if nm == 'Abs':
                x = ce(args[0]); return lambda d, e: M.absf(x(d, e))
            if nm == 'Log':
                x = ce(args[0])
                def flog(d, e):
                    v = x(d, e)
                    if v is None:
                        if M.null == 'YAY': return None
                        v = 0.0
                    if v <= 0:
                        if M.bolme == 'null': return None
                        if M.bolme == 'hata': raise Hata('log')
                        return float('-inf') if v == 0 else float('nan')
                    return math.log(v)
                return flog
            if nm == 'YilEkle':
                t, y = ce(args[0]), ce(args[1])
                def fy(d, e):
                    tv, yv = t(d, e), y(d, e)
                    if tv is None:
                        raise Hata('YilEkle(null)')   # null tarihte hata varsayimi (en sert)
                    return tv + 365.0 * yv
                return fy
            ad = alan_adi(nm, args)
            if ad is None: raise SyntaxError('sabit olmayan arguman ' + nm)
            if alanlar is not None: alanlar.add(ad)
            return lambda d, e, ad=ad: d[ad]
        raise SyntaxError(k)
    comp = [((s[1] if s[0] == 'asg' else None), ce(s[2] if s[0] == 'asg' else s[1])) for s in stmts]
    def run(d):
        env = {}; v = None
        for nm, f in comp:
            v = f(d, env)
            if nm is not None: env[nm] = M.asg(v)
        return M.asg(v)
    return run
