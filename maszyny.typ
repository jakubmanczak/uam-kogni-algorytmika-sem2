#let title = "Maszyny Turinga - Podstawy algorytmiki"
#let author = "Jakub Mańczak"

#set text(lang: "pl")
#set document(title: title, author: author)
#set page(
  header: align(center + horizon)[
    #author #h(1fr) #title
    #v(-8pt)
    #line(length: 100%, stroke: .5pt)
  ],
  footer: align(center)[#context [#counter(page).display()]]
)
#set heading(numbering: "1.")
#set par(justify: true)
#show heading: it => [
  #set align(left)
  #set text(
    if it.level == 1 { 12pt } else { 11pt },
    weight: if it.level == 1 { 600 } else { 500 }
  )
  #block(smallcaps(if it.numbering != none {
    [#counter(heading).display(it.numbering) #it.body]
    v(6pt)
  } else {
    it.body
  }))
]

= Wprowadzenie zapisu formalnego

Na potrzeby dokumentu wprowadza się poniżej określone notacje:
+ Literą $Gamma$ oznacza się alfabet, czyli zbiór wartości reprezentowalnych w krotkach taśmy.
+ Literą $Q$ oznacza się zbiór możliwych stanów maszyny.
+ Pod hasłem „Program” umieszcza się instrukcje dla maszyny, zapisane jak następuje: \
  $(Q_A, Gamma _A) -> (Q_B, Gamma _B, P)$, gdzie:
  - $Q_A$ i $Gamma _A$ oznaczają stan maszyny i odczytaną wartość z krotki,
  - $Q_B$ i $Gamma _B$ oznaczają nowy stan maszyny i nową wartość w krotce,
  - $P$ wyznacza kierunek przesunięcia głowicy i przyjmuje wartości:
    - $R$ (w prawo),
    - $L$ (w lewo),
    - $-$ (bez przesunięcia).
+ Zakłada się, że głowica startuje ustawiona na pierwszej (najbardziej znaczącej) krotce liczby.

#v(1cm)

= Maszyna Turinga: do zamiany wszystkich „a” na „b”, „b” na „c”, „c” na „a”.
$ Gamma = { a, b, c, #sym.nothing } #h(1cm) Q = { q_0, q_1 }, "gdzie" cases(
  q_0 colon "stan końcowy",
  q_1 colon "stan początkowy"
) $

#align(center)[
  Program: \
  $(q_1, a) -> (q_1, b, R)$ \
  $(q_1, b) -> (q_1, c, R)$ \
  $(q_1, c) -> (q_1, a, R)$ \
  $(q_1, #sym.nothing) -> (q_0, #sym.nothing, -)$
]

= Maszyna Turinga: do inkrementacji liczby w systemie trójkowym
$ Gamma = { 0, 1, 2, #sym.nothing } #h(1cm) Q = { q_0, q_1, q_2 }, "gdzie" cases(
  q_0 colon "stan końcowy",
  q_1 colon "stan początkowy",
  q_2 colon "stan inkrementacji",
) $

#align(center)[
  Program: \
  $(q_1, 0) -> (q_1, 0, R)$ \
  $(q_1, 1) -> (q_1, 1, R)$ \
  $(q_1, 2) -> (q_1, 2, R)$ \
  $(q_1, #sym.nothing) -> (q_2, #sym.nothing, L)$ \
  $(q_2, 2) -> (q_2, 0, L)$ \
  $(q_2, 0) -> (q_0, 1, L)$ \
  $(q_2, 1) -> (q_0, 2, -)$ \
  $(q_2, #sym.nothing) -> (q_0, 1, -)$
]

#pagebreak()
= MT: do dodania dwóch liczb unarnych oddzielonych zerem
$ Gamma = { 0, 1, #sym.nothing } #h(1cm) Q = { q_0, q_1, q_2 }, "gdzie" cases(
  q_0 colon "stan końcowy",
  q_1 colon "stan początkowy",
  q_2 colon "stan wyrównywania",
) $

#align(center)[
  Program: \
  $(q_1, 1) -> (q_1, 1, R)$ \
  $(q_1, 0) -> (q_1, 1, R)$ \
  $(q_1, #sym.nothing) -> (q_2, #sym.nothing, L)$ \
  $(q_2, 1) -> (q_0, #sym.nothing, -)$
]

= MT: która wykonuje odejmowanie liczb podanych w zapisie unarnym.
Zakłada się, że druga liczba jest równa lub mniejsza od pierwszej.

$ Gamma = { 0, 1, #sym.nothing } \ Q = { q_K, q_P, q_1 }, "gdzie" cases(
  q_K colon "stan końcowy",
  q_P colon "stan początkowy",
  q_1 colon "stan pierwszy",
  q_2 colon "stan drugi"
) $

#align(center)[
  Program: \
  $(q_P, 1) -> (q_P, 1, R)$ \
  $(q_P, 0) -> (q_1, 0, R)$ \
  $(q_1, 1) -> (q_2, 0, L)$ \
  $(q_2, 0) -> (q_2, 0, R)$ \
  $(q_2, 1) -> (q_1, 0, R)$ \
  $(q_1, 0) -> (q_1, 0, R)$ \
  $(q_1, #sym.nothing) -> (q_K, #sym.nothing, -)$
]

= MT: do inkrementacji liczby w systemie binarnym
$ Gamma = { 0, 1, #sym.nothing } #h(1cm) Q = {q_K, q_P, q_1}, "gdzie" cases(
  q_K & ": stan końcowy",
  q_P & ": stan początkowy",
  q_1 & ": stan inkrementacji"
) $

#align(center)[
  Program: \
  $(q_P, 1) -> (q_P, 1, R)$ \
  $(q_P, 0) -> (q_P, 0, R)$ \
  $(q_P, #sym.nothing) -> (q_1, #sym.nothing, L)$ \
  $(q_1, 0) -> (q_1, 1, L)$ \
  $(q_1, 1) -> (q_K, 0, -)$ \
  $(q_1, #sym.nothing) -> (q_K, 1, -)$ \
]

#pagebreak()
= MT: do dekrementacji liczby w systemie binarnym
$ Gamma = { 0, 1, #sym.nothing } #h(1cm) Q = { q_K, q_P, q_1 }, "gdzie" cases(
  q_K & ": stan końcowy",
  q_P & ": stan początkowy",
  q_1 & ": stan dekrementacji"
) $

#align(center)[
  Program: \
  $(q_P, 1) -> (q_P, 1, R)$ \
  $(q_P, 0) -> (q_P, 0, R)$ \
  $(q_P, #sym.nothing) -> (q_1, #sym.nothing, L)$ \
  $(q_1, 0) -> (q_1, 1, L)$ \
  $(q_1, 1) -> (q_K, 0, -)$ \
]

= Maszyna Turinga: do dodania dwóch liczb w systemie binarnym
$ Gamma = { 0, 1, X, #sym.nothing}, "gdzie" cases(
  0 & ": wartości binarna 0",
  1 & ": wartości binarna 1",
  #sym.nothing & ": wartość pusta",
  X & ": rozdzielenie dwóch liczb"
) \
  Q = { q_K, q_P, q_(1..5) }, "gdzie" cases(
    q_K & ": stan końcowy",
    q_P & ": stan początkowy",
    q_1 & ": --",
    q_2 & ": --",
    q_3 & ": --",
    q_4 & ": --",
    q_5 & ": --",
  )
$

#align(center)[
  Przykładowa sekwencja taśmy:
  #table(
    columns: 10,
    [$#sym.nothing$], [$1$], [$1$], [$0$], [$1$], [$X$], [$1$], [$0$], [$0$], [$#sym.nothing$]
  )
]

#align(center)[
  Program: \
  $(q_P, 1) -> (q_P, 1, R)$ \
  $(q_P, 0) -> (q_P, 0, R)$ \
  $(q_P, X) -> (q_P, X, R)$ \
  $(q_P, #sym.nothing) -> (q_P, #sym.nothing, L)$ \
  $(q_1, 1) -> (q_2, 0, L)$ \
  $(q_1, 0) -> (q_1, 1, L)$ \
  $(q_2, 1) -> (q_2, 1, L)$ \
  $(q_2, 0) -> (q_2, 0, L)$ \
  $(q_2, X) -> (q_3, X, L)$ \
  $(q_3, 0) -> (q_4, 1, R)$ \
  $(q_3, 1) -> (q_3, 0, L)$ \
  $(q_3, #sym.nothing) -> (q_4, 1, R)$ \
  $(q_4, 1) -> (q_4, 1, R)$ \
  $(q_4, 0) -> (q_4, 0, R)$ \
  $(q_4, X) -> (q_5, X, R)$ \
  $(q_5, 0) -> (q_5, 0, R)$ \
  $(q_5, 1) -> (q_P, 1, R)$ \
  $(q_5, #sym.nothing) -> (q_K, #sym.nothing, -)$ \
]
