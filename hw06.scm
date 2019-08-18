;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (unique s)
    (if (null? s)
        nil
        (cons (car s) (filter (lambda (x) (not (eq? x (car s)))) (unique (cdr s))))))

(define (cons-all first rests)
    (map (lambda (x) (cons first x)) rests)
)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
    (cond (( = total 0) (list nil))
      ((or (< total 0) (null? denoms)) nil)
      (else (let ((denom (car denoms)) (rest-denoms (cdr denoms)))
                 (append (cons-all denom (list-change (- total denom) denoms))
                         (list-change total rest-denoms))))))



; Tail recursion
(define (replicate x n)
    (define (helper count lst-so-far)
        (if (= count 0)
            lst-so-far
            (helper (- count 1) (cons x lst-so-far))))
    (helper n nil))

(define (accumulate combiner start n term)
    (if (= n 0)
        start
        (combiner (accumulate combiner start (- n 1) term)
                (term n))))

(define (accumulate-tail combiner start n term)
 (if (= n 0)
    start
    (accumulate-tail combiner (combiner (term n) start) (- n 1) term)))

; Macros
(define-macro (list-of map-expr for var in lst if filter-expr)
    `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst)))
