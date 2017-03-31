## My experimental programming languages

- [Lalan](#lalan)
- [Obin](#obin)

This repository contains prototypes for experimental programming languages
Each language has it's own branch
They share many common features and code base with differences mainly in parser and compiler


### Common features

* Functional
* Unpure
* Eager
* Immutable
* Dynamic
* Experimental and unique syntaxes (at least not known by me before)
* Persistent data structures (lists, tuples, maps)
* Pattern matching inspired by Erlang and ML
* Lexical clojures and lambdas
* Usual number of primitives (if-else, let-in, try-catch)
* User defined operators
* User defined types
* Builtin single dispatch
* Various level of support for currying and partial application
* Stackless virtual machine
* Asymmetric coroutines
* All code written in Python

### List of languages

#### Obin

* Indentation-aware syntax inspired by F#, Haskell and Python
* Juxtaposition used for function application
* Automatic currying
* Union types (like ADT, but in dynamic language their usefulness somewhat diminished)
* Lazy evaluation via special syntax
* Smart way of handling ambidextra operators

##### [Repository](https://github.com/gloryofrobots/langs/tree/obin)

##### Example
```
fun foldl
    | f acc [] -> acc
    | f acc hd::tl -> foldl f (f hd acc) tl

fun foldr
    | f acc [] -> acc
    | f acc hd::tl -> f hd (foldr f acc tl)


fun split s
    | [] -> ([], [])
    | s@[x] -> (s, [])
    | x::y::xs ->
        (l, r) = split xs
        (x::l, y::r)

fun sort f s ->
    fun _merge s1 s2
        | [] ys -> ys
        | xs [] -> xs
        | x::xs y::ys ->
            if f x y then x :: _merge xs (y::ys)
            else y :: _merge (x::xs) ys

    fun _sort s
        | [] -> []
        | s @ [x] -> s
        | xs ->
            (ys, zs) = split xs
            _merge (_sort ys) (_sort zs)

    _sort s
----------------------------------------

fun nine_billion_names_of_god_the_integer () ->
    (string:join
        (seq:map
            (n => string:join_cast
               (seq:map (g =>
                            fun _loop n g ->
                                if g == 1 or n < g then 1
                                else
                                    (seq:foldl
                                        (
                                            q res => res + if q > n - g then   // even while if inside () inner expressions must be aligned
                                                              0
                                                           else
                                                            (_loop (n-g) q)
                                        )
                                        1
                                        (range 2 g))
                                end // end token removes if layout and adds readability
                            end n g) (range 1 n)) " ") // end token terminates function layout and allows to call function with arguments (n g)
            (range 1 25))
         "\n")
--------------------------
```

#### Lalan
* Original and clean syntax inspired by Lua and OCaml
* Whitespace unaware parser
* Widely known syntax for expressions
* Using parentheses for creating blocks of expression, similar to {} blocks in C or Java
* Support for partial application via special syntax
* Custom operators
* Name binding only via let-in expression

##### [Repository](https://github.com/gloryofrobots/langs/tree/lalan)

##### Example

```
fun add(x,y) = x + y

// more the one expression can be enclosed in parenthesis
// the result of such expression is the result of last expression
fun add_and_print(x,y) =
(
    io:print("x + y", x + y)
    x + y
)
fun foldl
    | (f, acc, []) = acc
    | (f, acc, hd::tl) = foldl(f, f(hd, acc), tl)


fun foldr
    | (f, acc, []) = acc
    | (f, acc, hd::tl) = f(hd, foldr(f, acc, tl))

fun split
    | [] = ([], [])
    | s@[x] = (s, [])
    | x::y::xs =
        let (l, r) = split(xs)
        in (x::l, y::r)


fun sort(f, s) =
    let
        fun _merge
            | ([], ys) = ys
            | (xs, []) = xs
            | (x::xs, y::ys) =
                if f(x, y) then x :: _merge(xs, y::ys)
                else y :: _merge(x::xs, ys)

        fun _sort
            | [] = []
            | s @ [x] = s
            | xs =
                let (ys, zs) = split(xs)
                in _merge(_sort(ys), _sort(zs))

    in _sort(s)

fun enum_from(num) =
    let co = coro:spawn(
        fun(yield, _from) =
            let
                fun _looper(num) =
                (
                   yield(num)
                   _looper(num + 1)
                )
            in
            (
                yield(_from)
                _looper(_from)
            )
        )
    in
    (
        co(num)
        co
    )

```
