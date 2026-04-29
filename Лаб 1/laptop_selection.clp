;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Expert system: Laptop selection
;;   (load "C:\\Users\\ayurb\\OneDrive\\Рабочий стол\\massel\\Лаб 1\\laptop_selection.clp")
;;   (reset)
;;   (run)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffacts start-facts
   (initial-fact))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; User interaction
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffunction ask (?question)
   (printout t ?question " (yes/no): " crlf)
   (bind ?response (read))
   (if (eq ?response y) then (return yes))
   (if (eq ?response n) then (return no))
   (return ?response))

(defrule collect-user-answers
   (initial-fact)
   =>
   (printout t crlf "Laptop selection expert system" crlf)
   (printout t "Answer the questions using yes or no." crlf crlf)

   (if (eq (ask "Do you need a laptop for modern games?") yes) then (assert (gaming)))
   (if (eq (ask "Do you plan to use it for programming?") yes) then (assert (programming)))
   (if (eq (ask "Do you need it mainly for study?") yes) then (assert (study)))
   (if (eq (ask "Do you need it mainly for office work and browsing?") yes) then (assert (office)))
   (if (eq (ask "Will you work with graphics or design applications?") yes) then (assert (graphics)))
   (if (eq (ask "Will you edit video or work with heavy media files?") yes) then (assert (video-editing)))
   (if (eq (ask "Do you often carry the laptop with you?") yes) then (assert (portable)))
   (if (eq (ask "Is long battery life important?") yes) then (assert (battery)))
   (if (eq (ask "Is a very low price important?") yes) then (assert (low-budget)))
   (if (eq (ask "Do you have a high budget?") yes) then (assert (high-budget)))
   (if (eq (ask "Do you want a light and thin laptop?") yes) then (assert (lightweight)))
   (if (eq (ask "Do you need a large screen?") yes) then (assert (large-screen)))
   (if (eq (ask "Do you need a lot of storage space?") yes) then (assert (large-storage)))
   (if (eq (ask "Is quiet operation important?") yes) then (assert (quiet)))
   (if (eq (ask "Do you plan to install Linux?") yes) then (assert (linux)))
   (if (eq (ask "Is a durable case important?") yes) then (assert (durable)))

   (assert (answers-collected))
   (printout t crlf "Recommendations:" crlf))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Recommendation rules
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule advise-gaming-laptop
   (answers-collected)
   (gaming)
   (high-budget)
   =>
   (printout t "- Gaming laptop: discrete graphics card, powerful CPU, 16-32 GB RAM, good cooling. Example model: ASUS ROG Zephyrus G14." crlf))

(defrule advise-budget-gaming-laptop
   (answers-collected)
   (gaming)
   (low-budget)
   =>
   (printout t "- Budget gaming laptop: entry-level discrete GPU, 16 GB RAM, focus on cooling over thin design. Example model: Lenovo LOQ 15." crlf))

(defrule advise-programming-workstation
   (answers-collected)
   (programming)
   (high-budget)
   =>
   (printout t "- Developer workstation: fast CPU, 32 GB RAM, SSD from 1 TB, comfortable keyboard. Example model: Lenovo ThinkPad P1." crlf))

(defrule advise-programming-student
   (answers-collected)
   (programming)
   (study)
   (low-budget)
   =>
   (printout t "- Student programming laptop: modern CPU, 16 GB RAM, 512 GB SSD, reliable keyboard. Example model: Acer Aspire 5." crlf))

(defrule advise-office-laptop
   (answers-collected)
   (office)
   (low-budget)
   =>
   (printout t "- Office laptop: energy-efficient CPU, 8-16 GB RAM, SSD, matte Full HD screen. Example model: Lenovo IdeaPad Slim 3." crlf))

(defrule advise-ultrabook
   (answers-collected)
   (portable)
   (battery)
   (lightweight)
   =>
   (printout t "- Ultrabook: thin body, low weight, long battery life, USB-C charging. Example model: Apple MacBook Air M2." crlf))

(defrule advise-business-laptop
   (answers-collected)
   (office)
   (durable)
   =>
   (printout t "- Business laptop: durable case, good keyboard, webcam, security features, warranty support. Example model: Lenovo ThinkPad T14." crlf))

(defrule advise-design-laptop
   (answers-collected)
   (graphics)
   (high-budget)
   =>
   (printout t "- Design laptop: color-accurate screen, 16-32 GB RAM, strong CPU/GPU, large SSD. Example model: Apple MacBook Pro 14." crlf))

(defrule advise-budget-design-laptop
   (answers-collected)
   (graphics)
   (low-budget)
   =>
   (printout t "- Budget design laptop: prioritize IPS display, 16 GB RAM and SSD; avoid very weak processors. Example model: ASUS Vivobook Pro 15." crlf))

(defrule advise-video-editing-laptop
   (answers-collected)
   (video-editing)
   =>
   (printout t "- Video editing laptop: powerful multi-core CPU, discrete GPU, 32 GB RAM if possible, fast SSD. Example model: ASUS ProArt Studiobook 16." crlf))

(defrule advise-large-screen-laptop
   (answers-collected)
   (large-screen)
   (not (portable))
   =>
   (printout t "- Large-screen laptop: 16-17 inch display, comfortable for home work but less portable. Example model: LG Gram 17." crlf))

(defrule advise-storage-focused-laptop
   (answers-collected)
   (large-storage)
   =>
   (printout t "- Storage-focused laptop: choose SSD from 1 TB or a model with an additional drive slot. Example model: Dell Inspiron 16 Plus." crlf))

(defrule advise-linux-laptop
   (answers-collected)
   (linux)
   =>
   (printout t "- Linux-friendly laptop: prefer popular business models with well-supported Wi-Fi and graphics. Example model: Dell XPS 13." crlf))

(defrule advise-quiet-laptop
   (answers-collected)
   (quiet)
   (not (gaming))
   (not (video-editing))
   =>
   (printout t "- Quiet laptop: energy-efficient processor, no discrete GPU, good cooling profile. Example model: Apple MacBook Air M3." crlf))

(defrule advise-balanced-laptop
   (answers-collected)
   (not (gaming))
   (not (video-editing))
   (not (low-budget))
   (not (high-budget))
   =>
   (printout t "- Balanced universal laptop: 16 GB RAM, 512 GB SSD, IPS screen, modern mid-range CPU. Example model: HP Pavilion 15." crlf))

(defrule finish
   (declare (salience -67))
   (answers-collected)
   =>
   (printout t crlf "Selection finished. Compare the printed options and choose the closest one." crlf))
