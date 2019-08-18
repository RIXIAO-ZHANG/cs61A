(define (hailstone x)
    (print x)
    (cond
        ((= x 1) 1)
        ((even? x) (+ 1 (hailstone  (/ x 2))))
        ((odd? x) (+ 1 (hailstone (+ (* x 3) 1))))
    ))
