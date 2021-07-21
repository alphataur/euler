(ns eulerclj.euler24
  (:gen-class))

(defn tails [coll]
  (take-while seq (iterate rest coll))
)

(defn inits [a-seq]
  (reverse (map reverse (tails (reverse a-seq)))))

(defn rotations [coll]
  (map concat (tails coll) (inits coll))
)

(defn permutations [a-set]
  (if (empty? a-set)
    (list ())
    (mapcat
     (fn [[x & xs]] (map #(cons x %) (permutations xs)))
     (rotations a-set))))


(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (permutations (range 3))))


