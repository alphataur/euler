(ns eulerclj.euler4
  (:gen-class))

(defn reverse-num [n]
  (map #(Character/digit % 10) (str n)))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (reverse-num 7292824305)))
