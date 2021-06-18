(ns eulerclj.euler4
  (:gen-class))

(defn is-palindrome [n]
  (let [repr (str n)]
   (= repr (apply str (reverse repr)))))


(defn solve []
  (for [i (range 100 999) j (range 100 999) :when (is-palindrome (* i j))]
    [(* i j) i j]
  )
)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (last (sort-by #(nth % 0) (solve)))))
