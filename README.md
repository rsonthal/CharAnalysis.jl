# CharAnalysis

This is a basic package to clean up text data and to do basic analysis. This works for both ascii and unicode strings.

# Documentation

`ngam(t,n)` - Given a `String t` and an `Integer n` it returns a dictionary with an ngram. These ngrams are character ngrams not words

`removeChar(t,c)` - Given a `String t` and a `Char c` this function removes all instances of `c` from `t`

`removeChars(t,c)` - Given a `String t` and a `Array{Char,1} c` this function removes all instances of `Char`s in `c` from `t`

`removeNumbers(t)` - Removes all numbers from the `String t`

`removePunctuation(t)` - Removes all punctuations from the `String t`

`keepChars(t,c)` - Given a `String t` and a `Array{Char,1} c` we remove all `Char`s from `t` that are *not* in `t`

`replaceWhitespace(t)` - Given a `String t` it replaces all white space Unicode characters that represent white space with U+0020

`condenseWhitepsace(t)` - Given a `String t` it takes all contigous segments of U+0020 and replaces it with U+0020. 

# Example Usage

Given a String `t` we can get a cleaned version by running the following lines of code

`t = removeNumbers(t)`
`t = removerPunctuation(t)`
`t = replaceWhitespace(t)`
`t = condenseWhitespace(t) `
`t = keepChars(t,c)`
