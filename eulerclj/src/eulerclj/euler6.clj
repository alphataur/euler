(ns eulerclj.euler6
  (:gen-class))

(defn solve []
  (reduce + (map #(* 2 (reduce * %)) (partition 2 1 (range 1 11))))
)
(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (solve))
)
