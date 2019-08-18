(define (partial-sums s)
    (cons-stream (car s)
     (map (lambda (x) (+ x (car s)))
    (partial-sums (cdr-stream s)))))
