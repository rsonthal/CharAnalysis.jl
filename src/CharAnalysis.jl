module Bigram

function ngram(t,n)
    gram = Dict{String,Int64}()
    T = collect(t)
    N = length(T)
    for i = 1:N-n+1
        s = String(T[i:i+n-1])
        if haskey(gram,s)
            gram[s] += 1
        else
            gram[s] = 1
        end
    end
    
    return gram
end

function removeChar(t,c)
    t = filter(e->e!=c,t)
    return t
end

function removeChars(t,c)
    t = filter(e->!(e in c),t)
    return t
end

function removeNumbers(t)
    c = ['0','1','2','3','4','5','6','7','8','9']
    t = removeChars(t,c)
    return t
end

function keepChars(t,c)
    return filter(e -> (e in c),t)
end

function removePunctuation(t)
    c = ['.',',','\'','?','!','(',')','{','}','[',']','&', ':', ';', '\"', '/','>','<','|']
    t = removeChars(t,c)
    return t
end
                    
C = ['\u0009','\u000A','\u000B','\u000C','\u000D','\u0085','\u00A0','\u1680',
         '\u2000','\u2001','\u2002','\u2003','\u2004','\u2005','\u2006','\u2007',
         '\u2008','\u2009','\u200A','\u2028','\u2029','\u202F','\u205F','\u3000']

function replaceWhitespace(t)
    T = collect(t)
    for i = 1:length(T)
        if T[i] in C
            T[i] = ' '
        end
    end
    return String(T)
end

function condenseWhitespace(t)
    T = collect(t)
    newT = ""
    newT = newT*T[1]
    for i = 2:length(T)
        if (T[i] == ' ' && T[i-1] != ' ') || T[i] != ' '
            newT = newT*T[i]
        end
    end
    
    T = collect(newT)
    s=1
    e=length(T)
    if T[1] == ' '
        s = 2
    end
    if T[e] == ' '
        e -= 1
    end
    
    
    return newT[s:e]
end

end