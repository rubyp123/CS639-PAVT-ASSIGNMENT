   if (:w > :y)
    [
        if (:y > :w)
        [
            if (:z > 50)
            [
               left 60
            ]
            else
            [
               left 75
            ]
        ]    
    ]
    else
    [
        if (:y > 40)
        [  
            if (:z >10)
            [
                forward 80
            ]
            else
            [
                backward 40
            ]
        ]
        else
        [ 
            if (:z > 10)
            [   
                right 60
            ]
            else
            [   
                left 30
            ]
        ]
    ]
