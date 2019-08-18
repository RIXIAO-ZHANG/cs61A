"""
The first version of range takes linear space
The first version of range takes constant space
"""

(define (range a b)
        (if (>= a b) nil
                    (cons a (range (+ a 1) b))))


(define (range-stream a b)
    (if (>= a b) nil
                (cons-stream a (range-stream (+ a 1) b))))



"""
Inter stream
"""
(define (int-stream start)
    (cons-stream start (int-stream (+ 1 start))))


"The function Prefix takes a stream that's why we use (cdr-stream x)"
(define (prefix x k)
    (if (= k 0) ()
                (cons (car s) (prefix (cdr-stream x) (- k 1)))))

"The function square-stream takes a stream that's why we use (cdr-stream x)"
(define (square-stream x)
    (cons-stream (* (car x) (car x)) (square-stream (cdr-stream x))))


"The rest of a constant stream is the constant stream"
(define ones (cons-stream 1 ones))

"Combine two streams by separating each into car and cdr"
(define (add-stream s t)
        (cons-stream (+ (car s) (car t))
                    (add-stream (cdr-stream s) (cdr-stream t))))

"With ones stream and add-stream function we could write a more compact expression of int-stream"
(define ints (cons-stream 1 (add-stream ones  ints)))
"1,2,3,4,5..."

"Sequence Processing/Manipulation"

"Map"
(define (map-stream f s)
        (if (null? s)
            nil
            (cons-stream (f (car s)) (map-stream f (cdr-stream s)))))
"Filter"
(define (filter-stream f s)
        (if (null? s)
            nil
            (if (f (car s))
                (cons-stream (car s) (filter-stream f (cdr-stream s)))
                (filter-stream f (cdr-stream s)))))

"Reduce"
(define (reduce-stream f s start)
        (if (null? s)
            start
            (reduce-stream f (cdr-stream s) (f start (car s)))))
