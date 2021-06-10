(ns eulerclj.euler2
  (:gen-class))

(def fibonacci
  (lazy-cat [0 1] (map + (rest fibonacci) fibonacci)))

(defn solve2 [bound]
  (reduce + (filter even? (take-while #(< % bound) fibonacci))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (solve2 4000000)))
