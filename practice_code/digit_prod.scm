(define (digit-prod n)
    (if (< n 10)
        n
        (* (modulo n 10) (digit-prod (quotient n 10)))))
