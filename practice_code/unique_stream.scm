(define (unique-stream s)
    (define (helper s seen)
        (cond ((null? s) '())
            ((contain? seen (car s))  (helper (cdr-stream s) seen))
            (else  (cons-stream (car s) (helper (cdr-stream s) (cons (car s) seen))))))
    (helper s  nil))


(define (unique-stream s)
    (cons-stream (car s)
     (filter-stream (lambda (x) (not (= x (car s))))
         (cdr-stream s)))
