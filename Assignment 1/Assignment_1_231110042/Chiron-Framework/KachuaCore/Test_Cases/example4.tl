pendown 
:a = :x
:b = :y
:c = :z
repeat 5[
    if :a>:b[
        if(:a>:c)[
            forward 100
        ]
    ]
    
    if :b>:c[
        if(:b>:c)[
            right 100
        ]
    ]
    
    if :c>:a[
        if(:c>:b)[
            backward 100
        ]
    ]

    :a=:x+:y
    :b=:y+:z
    :c=:x+:z
    
]