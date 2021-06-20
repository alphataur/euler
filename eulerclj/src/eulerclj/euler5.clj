(ns eulerclj.euler5
  (:gen-class))

(defn gcd [a b]
  ;use loop please!
  (if (zero? b)
    a
    (gcd b (mod a b))
  )
)
; gcd euclidean
; 1920 1080
; 840 1080
; 1080 840
; 240 840
; 840 240
; 120 240
; 

(defn lcm [a b]
  (/ (* a b) (gcd a b))
)


(defn -main
  "probably the slickest solution in clojure i've produced till now"
  [& args]
  (println (reduce lcm (range 1 10))))
