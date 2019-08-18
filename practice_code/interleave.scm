(define (incr-interleave s1 s2)

    (define (helper s1 s2 count n)
        (if (= count n)
            (helper s2 s1 0 (+ 1 n))
            (cons-stream (car s1) (helper (cdr-stream s1) s2 (+ 1 count) n))))
    (helper s1 s2 0 1))
