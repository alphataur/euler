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


(defn sum-square-form [upper-bound]
  (/ (* upper-bound (inc upper-bound) (inc (* 2 upper-bound))) 6)
)

(defn square-sum-form [upper-bound]
  (let [i (/ (* upper-bound (inc upper-bound)) 2)] (* i i))
)

(defn mathy [upper-bound]
  (- (square-sum-form upper-bound) (sum-square-form upper-bound))
)

(defn combinations [n]
  (for [i (range 1 (inc n)) j (range 1 (inc n)) :when (not (= i j))] (vector i j)))


(defn mathy-diff [upper-bound]
  (let [comb (combinations upper-bound)]
    (reduce + (map #(reduce * %) comb))
  )
)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (mathy 100))
)
