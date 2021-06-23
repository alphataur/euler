(ns eulerclj.euler7
  (:gen-class))

(defn factors [n]
  (filter #(zero? (mod n %)) (range 2 (dec n)))
)

(def memo-factors
  (memoize factors)
)

(defn is-prime [n]
  (= (count (memo-factors n)) 0)
)



(defn next-prime [curr-prime]
  (loop [i (inc curr-prime)]
    (do (println i) (if (is-prime i)
      i
      (recur (inc i))
    )
  ))
)



(defn prime-gen [idx]
  (loop [i 1 res 2]
    (if (= i idx)
      res
      (recur (inc i) (next-prime res))
    )
  )
)



(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (prime-gen 10001)))


;"""
;next-prime [res]
;(loop [i (inc res)]
;  (if (is-prime i)
;    i
;    (recur (inc res))
;  )
;)
;prime-gen [idx]
;
;(loop [i 1 res 2]
;  (if (= i idx)
;    res
;    (recur (inc i) (next-prime res))
;  )
;)
;
;"""
