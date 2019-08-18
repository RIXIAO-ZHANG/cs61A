(define (sqrt x)
    (define (good-enough? guess)
        (< (abs(- (square guess) x)) 0.001) #body of the nested definition
    )# good-enough nested definition ends

    (define (improve guess)
        (average guess (/ x guess))#body of the nested definition
    )# imporve guess nested definition ends

    (define (sqrt-iter guess)
        (if (good-enough? guess)
                guess
                (sqrt-iter (improve guess))
    )#body of the nested definition
    )# sqrt-iter nested definition ends

    (sqrt-iter 1.0)
)#sqrt definition ends


(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
	(sqrt-iter 1.0))
(sqrt 9)
