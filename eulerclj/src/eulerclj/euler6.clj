(ns eulerclj.euler6
  (:gen-class))

(defn square-sum [upper-bound]
  (let [i (/ (* upper-bound (inc upper-bound)) 2)]
    (* i i)
  )
)

(defn sum-square [upper-bound]
  (
   ->> (range (inc upper-bound))
   (map #(* % %))
   (reduce +)
  )
)

(defn naive-solver [upper-bound]
  (- (square-sum upper-bound) (sum-square upper-bound))
)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (naive-solver 100))
)
