(ns eulerclj.euler1
  (:gen-class))

(defn solve [bound]
  (reduce + (filter #(or (= 0 (mod % 3)) (= 0 (mod % 5))) (range 1 bound))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (solve 1000)))
