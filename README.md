# Obin programming language

Obin is a small, unpure functional programming language with immutable datastructures.
It exists currently only as prototype written in python and I do not plan to continue it's developing.

## Currently implemented features
* Modern expressive functional syntax which resembles something between Erlang and F#.
* Handwritten, extensible operator precedence parser with support of indentation layouts and juxtaposition operator
* Module system as a cross between Python, Haskell and Lua
* Polymorphism engine similar to Clojure's protocols but with possibility to dispatch not only on first argument
* Automatic carrying with simple push and pop model
* Stackless, stack based virtual machine
* Persistant data structures (lists, vectors, maps), shamelessly stolen from [Pixie](https://github.com/pixie-lang/pixie). 
* Pattern matching, let-in blocks, clojures, try-catch-finally, abstract data types
* Assymetric coroutines
 

Syntax example
```
//NOTE Obin does not support tabs in any way
//infix operators, right left associativity
// operator, function name, precedence
infixr := := 10
infixl <| <| 15
infixl |> |> 20
infixl << << 25
infixl >> >> 25

//operators implementation
//F# like carrying operators
fun |> x f -> f x
fun <| f x -> f x
fun >> f g x -> g (f x)
fun << f g x ->  f (g x)

//operator as a polymorphic function
trait MutRef for self of Ref
    def := self value
    
//almost all base operators like + - * / etc are polymorphic functions which can be implemented for user types
type Data value
extend Data
   with MutRef
     def := self value -> obin:mutable:put self #value value

trait Val for self
    def val self

type Option
    | Some val
    | None

extend Option
    with Val
        def val self ->
            match self with
                | x of Some -> x.val
                | x of None -> x

type Point2 x y

type Vec2 p1 p2

trait Add for self
    def add self a

implement Add for Point2
    def add self other
        | _ p2 of Point2 -> Point2 (self.x + p2.x) (self.y + p2.y)
        | _ i of Int -> Point2 (self.x + i) (self.y + i)
        | _ v of Vec2 -> add (Vec2 self self) v

implement Eq for Point2
    def == self other of Point2 ->
            self.x == other.x and self.y == other.y
    def != self other of Point2 -> not (self == other)

// simple function for Seq trait
fun foldr func accumulator coll
    | f acc [] of Seq -> acc
    | f acc (hd::tl) of Seq -> f hd (foldr f acc tl)

// () is unit type (empty tuple). Every function must have at least one argument
fun test () ->
   // indentation is important
   // but layouts are flexible and you can call lambdas after creation, immediately
   io:print (lam x y z ->
               a = x + y z
               b = a + 42
               b * 24
             end 1 2 3)
    //tuples
    (x,y,z) = (1,2.334353252,3)
    //lists
    let x::xs = [1,2,3,4,5] in
        affirm:is_equal x 1
        affirm:is_equal xs [2,3,4,5]
    //maps strings, and symbols
    Alice = {name="Alice", symbol_name = #Alice }
    Alice.name == ALice.symbol_name
    
    // = is not assignment, but matching, like in Erlang
    a = 1 // 1
    a = 2 // throws  
    1 = 1 // 1
    2 = 1 // throws 
    
    // Varname @ pattern binds result of pattern to variable Varname
    {a=[x,y,...z], B @ b="I am B", c of Float, D@d={e=(x,y,...zz)}} =
                               {a=[1,2,3,4,5], b="I am B", c=3.14, d={e=(1,2,3,4,5)}}
                    

    // if function call arguments lays on multiple lines ,we can use syntax f . arg1 . arg1 which is the same as Haskell's $ but does not creates carried functions
    // important! spaces are very important, for example human.name is member access notation and human . name is function call
    affirm:is_equal try
                        throw (1,2,"ERROR")
                    catch
                        | err @ (1, y, 3) -> #first
                        | (1,2, "ERROR@") -> #second
                        | err @ (1, 2, x) -> #third
                    finally ->
                        (#fourth, err, x)
                    end . // -> this is obin syntax for multiline arguments
                    (#fourth, (1, 2, "ERROR"), "ERROR")
    
    // another way to express multiline call is to use parens in a very lisp like manner
    (affirm:is_equal 
          (lam x y z
            | 1 2 3 -> 11
            | 2 4 5 -> 22
          end
                    1
                        2

                         3) 11)
    //conditions and layouts
    affirm:is_false if 5 == 4 then True else False
    affirm:is_equal (if 13 == 12 then 42 * 2 else if 13 == 14 then 12 * 2 else 1 end end) 1
    affirm:is_equal if x == 13 then 1 + 1
                    elif x == 14 then 2 + 2
                    elif x == 15 then 3 + 3
                    else 4 + 4 end . // -> ` .` syntax for multiline
                    8
    //pattern matching
    //function signature is mandatory, even if it is very simple
    fun f2 a | 0 -> 1
             | 1 -> 2
             | 2 -> 3
    
    match (1,2,3) with | (x,y,z) -> 2
                       | _ -> 1
                       
    fun prefix_of coll1 coll2
        | [hd, ...pre_tail] hd::tail -> prefix_of pre_tail tail
        | [] s -> True
        | [_, ..._] s -> False
    --------------------------------------------------
    // more than five ----- dashes interpreted as `end` token
    // [el, el2, ...tl] is equivalent to el1::el2::tl in pattern matching, but it can be also used for tuples as (el1, el2, ...tl)
//end here is not necessarry, it will be inserted automatically according to indentation layout
end 
// many more examples, such as abstract data types, lazy evaluation, transducers, traits can be found in obin_py/tests/obin
```

## Known problems
* Error reporting is very bad, it does more harm than good now
* Obin has problem with prefix operator - 
    For example if you type
    io:print -1 it will be interpreted as sexpr (- io:print 1) you need to type
    io:print (-1) instead
* Custom operators can be created but they will be exported only from prelude, if declared in other module they will remain local
* Lack of macrosses
* Lack of tail call elimination and other optimizations common to functional languages
* Because every function call in obin is trampolined as one VM loop iteration, there are no way to easily call obin code from native code
* Current obin implementation is a draft, so many things need to be optimized for speed and memory


Obin scripts are placed in test/obin, where
* obin_py/test/obin/\_\_lib__ folder contains obin stdlib
* obin_py/test/tests folder contains testing scripts

Some code (big enums, repeating blocks) generated from scripts in obin_py/generators. Generation is not automatic, I manually run some script and copy paste it's stdout.
To run interpreter
```
cd obin_py 
python  targetobin.py test/obin/main.obn
```
Program will run painfully slowly with stock python so I recomend using pypy instead
You may need pypy toolchain in the path see ```obin_py/runobin.sh``` for details.
Obin does not compiles with RPython currently, but it can be done with some effort.


Obin may not have any practical interest but it may be usefull for people who begin to study compilers and virtual machines
Project split into two folders obin_c and obin_py. Folder obin_c is obsolete, I keep it with hope of return to the project at some time.


I abandon project because of
1. Such language (immutable and functional aka Erlang) needs large ecosystem and well suited for complicated parallel programming but I plan it as a small embeddable language, so I don't have confidence now that i am designing something usefull
2. Automatic carrying is very error prone in dynamic languages, but without it syntax with juxtaposition has little sense
3. I understand that minimal and expressive syntax are also terse and very hard to read with screen readers and accesibility is very important for me.
4. I want to experiment with type systems and may be switch to another language
