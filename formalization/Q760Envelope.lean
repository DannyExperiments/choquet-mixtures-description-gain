import Std
namespace Envelope
/-- Finite geometric mixture with its unused tail mass assigned to t. -/
def blend (t : Rat) : List Rat → Rat
  | [] => t
  | x :: xs => (x + blend t xs)/2
def discount (c : Rat) : Nat → Rat
  | 0 => c
  | n+1 => discount c n/2

theorem floor (t c : Rat) (initial good : List Rat)
    (hp : ∀ x ∈ initial, 0 ≤ x) (hg : ∀ x ∈ good, c ≤ x) (ht : c ≤ t) :
    discount c initial.length ≤ blend t (initial ++ good) := by
  have suffix : c ≤ blend t good := by
    induction good with
    | nil => exact ht
    | cons x xs ih =>
      have h := hg x (by simp)
      have h' := ih (fun y hy => hg y (by simp [hy]))
      simp only [blend]; grind
  induction initial with
  | nil => exact suffix
  | cons x xs ih =>
    have h := hp x (by simp)
    have h' := ih (fun y hy => hp y (by simp [hy]))
    simp only [List.cons_append, discount, blend]; grind
#print axioms floor
end Envelope
