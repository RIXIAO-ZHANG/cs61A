(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
    (map-stream (lambda (x) (+ 3 x)) (cons-stream 0 multiples-of-three)))

(define (rle s)
    (define (helper str count)
        (cond
            ((null? str) '())
            ((null? (cdr-stream str)) (cons-stream (list (car str) count) nil))
            ((= (car str) (car (cdr-stream str))) (helper (cdr-stream str) (+ 1 count)))
            (else (cons-stream (list (car str) count) (helper (cdr-stream str) 1)))))
    (helper s 1))
