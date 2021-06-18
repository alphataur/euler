(ns eulerclj.euler3
  (:gen-class))

(defn divisible? [a b]
  (zero? (mod a b))
)

(defn factors [n]
  (filter #(divisible? n %) (range 2 (/ n 2)))
)


(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (empty? (factors 7))))
