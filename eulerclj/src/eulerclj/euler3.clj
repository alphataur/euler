(ns eulerclj.euler3
  (:gen-class))

(defn is-factor [a b]
  (zero? (mod a b)))

(defn factors [n]
  (filter #(is-factor n %) (range 2 (inc (Math/sqrt n)))))

(defn- test-prime
  "Determine if a number is prime by looping through divisors"
  [x]
  (loop [iter 5 top (Math/sqrt x)]
    (cond
      (> iter top) true
      (or (zero? (mod x iter))
          (zero? (mod x (+ 2 iter)))) false
      :else (recur (+ 6 iter) top))))

(defn is-prime
  "Determines if a given integer is prime."
  [x]
  (cond
    (<= x 3) (< 1 x)
    (or (zero? (mod x 2))
        (zero? (mod x 3))) false
    :else (test-prime x)))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (last (filter is-prime (factors 600851475143)))))
