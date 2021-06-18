(ns eulerclj.euler3
  (:gen-class))

(defn first-factor [n]
  (loop [i (int (/ n 2))]
    (if (< i 2)
      1
      (if (zero? (mod n i))
        i
        (recur (dec i))
      )
    )
  )
)


(defn is-prime [n]
  (< (first-factor n) 2)
)

(defn solver [n]
  (
   loop [current (int (/ n 2)) factor (first-factor n)]
  )
)





(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (solver 13195)))
