(define (deep-reverse lst)
    (cond
        ((null? lst) nil)
        ((list? (car lst)) (append   (deep-reverse (cdr lst))  (list (deep-revers (car lst)))))
        (else
            (append (deep-revers (cdr lst)) (list (car lst))))))
