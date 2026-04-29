;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Expert system: Simple vacation selection
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffacts start-facts
    (initial-fact))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Function to ask a question
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffunction ask (?question)
    (printout t ?question " (yes/no): " crlf)
    (bind ?response (read))
    (return ?response)
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Rules to get user answers
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule ask-active
    (initial-fact)
    =>
    (bind ?a (ask "Do you like active rest?"))
    (if (eq ?a yes) then (assert (active)) else (assert (passive)))
)

(defrule ask-nature
    =>
    (bind ?a (ask "Do you like nature?"))
    (if (eq ?a yes) then (assert (nature)))
)

(defrule ask-beach
    =>
    (bind ?a (ask "Do you like beach vacations?"))
    (if (eq ?a yes) then (assert (beach)))
)

(defrule ask-mountains
    =>
    (bind ?a (ask "Do you like mountains?"))
    (if (eq ?a yes) then (assert (mountains)))
)

(defrule ask-comfort
    =>
    (bind ?a (ask "Is comfort important for you?"))
    (if (eq ?a yes) then (assert (comfort)))
)

(defrule ask-excursions
    =>
    (bind ?a (ask "Do you like excursions?"))
    (if (eq ?a yes) then (assert (excursions)))
)

(defrule ask-extreme
    =>
    (bind ?a (ask "Do you like extreme activities?"))
    (if (eq ?a yes) then (assert (extreme)))
)

(defrule ask-home
    =>
    (bind ?a (ask "Do you prefer staying at home?"))
    (if (eq ?a yes) then (assert (home)))
)

(defrule ask-abroad
    =>
    (bind ?a (ask "Do you like traveling abroad?"))
    (if (eq ?a yes) then (assert (abroad)))
)

(defrule ask-walking
    =>
    (bind ?a (ask "Do you like long walks?"))
    (if (eq ?a yes) then (assert (walking)))
)

(defrule ask-citylife
    =>
    (bind ?a (ask "Do you like city life and nightlife?"))
    (if (eq ?a yes) then (assert (citylife)))
)

(defrule ask-relaxation
    =>
    (bind ?a (ask "Do you like relaxing vacations?"))
    (if (eq ?a yes) then (assert (relaxation)))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Simple recommendations
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule advise-beach
    (passive) (beach) (comfort)
    =>
    (printout t "Recommended vacation: Beach holiday." crlf)
)

(defrule advise-mountains
    (active) (mountains)
    =>
    (printout t "Recommended vacation: Mountain tourism." crlf)
)

(defrule advise-city
    (excursions) (citylife)
    =>
    (printout t "Recommended vacation: City tourism." crlf)
)

(defrule advise-extreme
    (active) (extreme)
    =>
    (printout t "Recommended vacation: Extreme tourism." crlf)
)

(defrule advise-home
    (home)
    =>
    (printout t "Recommended vacation: Stay at home." crlf)
)

(defrule advise-abroad
    (active) (abroad)
    =>
    (printout t "Recommended vacation: Travel abroad." crlf)
)

(defrule advise-eco
    (nature) (passive)
    =>
    (printout t "Recommended vacation: Eco tourism." crlf)
)

(defrule advise-resort
    (comfort)
    =>
    (printout t "Recommended vacation: Resort vacation." crlf)
)

(defrule advise-hiking
    (walking) (active)
    =>
    (printout t "Recommended vacation: Hiking tours." crlf)
)

(defrule advise-cultural
    (excursions)
    =>
    (printout t "Recommended vacation: Cultural tourism." crlf)
)

(defrule advise-youth
    (citylife)
    =>
    (printout t "Recommended vacation: Youth tourism." crlf)
)

(defrule advise-family
    (comfort) (passive)
    =>
    (printout t "Recommended vacation: Family vacation." crlf)
)