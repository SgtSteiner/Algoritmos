"""
Problem #19 Matching Brackets

http://www.codeabbey.com/index/task_view/matching-brackets

We are given strings containing brackets of 4 types - round (), square [], curly {} and angle <> ones. The goal is
to check, whether brackets are in correct sequence. I.e. any opening bracket should have closing bracket of the same
type somewhere further by the string, and bracket pairs should not overlap, though they could be nested:

(a+[b*c] - {d/3})  - here square and curly brackets are nested in the round ones

(a+[b*c) - 17]     - here square brackets overlap with round ones which does not make sense

Input data will contain number of testcases in the first line.
Then specified number of lines will follow each containing a test-case in form of a character sequence.
Answer should contain 1 (if bracket order is correct) or 0 (if incorrect) for each of test-cases, separated by spaces.

Note that all non-bracket characters could be safely ignored!

Test data:
19
<[[-<{ }->{t}{a}][g<^>{u}]<<%>a>{]>[c](tc(x(a[e])(f))}v)<^>
{}[({d}d)<c{v}>a]{(<*>{c}(%)[(/)h]a)x}([y][ ]d)
{a}({d}c<->[ ]<<->d>{u}{t}{-}[^(z)<^<w>>]{%}){ }{g} ]{u}{w}
</>{t}{[g]v}[v{^}]{}{v}[{d{ }}^]((y{z}[c])< >[b]-)<e>
(h{^}){(a)[d]y<b>[t]<<c>{t}y{v}(/){ }(y)>}<^>{}{-{{h}a}<+>}(f)
{x(<w{+}> )[x]<w>(+)<->}<e><y>[[x]b]{w}[y]<{< >(^ t]){u}v}>
[<u{b}<[z][<u>t]y[+]{%}><a>[t][{y}f{h}]>]{*{e}}{/<^>}<t<>{y{u}}^>
{w}<u><[(u)[h] ]^>[(h[w])][ ]<x{{-}h{x}}>[*](w)
[([z] {*}(v<v>)){c}<-(b)>[{c}z]g] e>(([*]y)( <a>(w){f}{(z)z})<b>)
<[w]{g}(g)[y[h]<g>]<[y]+>[v{e}{x[-]}[y][a]](+)(<+>{y}w)>{<y>^}(z)
{z}{e}<>[{+}f][{{c}t}{{< >-{[( )z]c}}^}/][(<t>w)<d>^]
(g)<>( )[t][<z>h](<g[c]{w}>^)[y]<<(x<x>){(d)-} >(h)[a<+>]x>
<%><(f[f]){x}w><z( )><(/)<y>{u}[y](f)< {x}{+}( )>>(w)(%)
((c){{([d]%)[^]+( [^])}a}{(a<g[x]>)y({z}/)[ ]}[t])<< >{*}( )/>
{<<+>d>}([+]( )*{^}{{h}{f(e)}{g}{-[t][v]}}/)
<[[t](a<z>(u))(+{ })/][{t}x]{w(<{y}d>w)<<[[*]c]/>c>}{t}>
[(a}<y(h)>a]{[[x(f)][f]{/}+]{^)<x>}{t[+]}{b}{g}
(z){[[f]<+{x[g]{t}}>(< >v)[ [f]][-]([d]z<+>)w(y)]}{b}
(<g>{w}t{z})[ ](u[t])[x{[+]z}]<u><y>{-}(/)(z)(v){(%)%</>}[]

"""

OPEN = "([{<"
CLOSE = ")]}>"


def calc_matching_brackets(datos):
    brackets = []
    res = True
    for dato in datos:
        if dato in OPEN:
            brackets.append(dato)
        elif dato in CLOSE:
            if not brackets:
                res = False
                break
            else:
                if brackets[-1] == OPEN[CLOSE.find(dato)]:
                    brackets.pop()
                else:
                    res = False
                    break
    return int(not brackets and res)


if __name__ == "__main__":
    num_data = int(input())
    results = [calc_matching_brackets(input()) for x in range(num_data)]
    print(" ".join(map(str, results)))
