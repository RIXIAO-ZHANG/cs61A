(define (multicompose funcs)
    (lambda (x)
    (if (null? funcs)
        nil
        ((car func) (multicompose (cdr funcs)) x))))
