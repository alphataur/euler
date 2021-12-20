(ns eulerclj.euler10
  (:gen-class)
  (:require [clojure.set])
)

(defn sieve-4 []
  (loop [nums (set (cons 2 (range 3 2000000 2))) n 3]
    (if (> (* n n) 2000000) (reduce + nums)
        (recur (clojure.set/difference nums (range (* n n) 2000000 n)) (+ n 2)))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (sieve-4)))
