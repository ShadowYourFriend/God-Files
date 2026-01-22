class Soul:
    def __init__(self, name):
        self.name = name
        self.state = "Sin"
        self.burden = 100  # Representing spiritual weight
        self.has_faith = False

    def repent(self):
        """Turning away from the old path."""
        print(f"\n[Repentance] {self.name} acknowledges the burden.")
        self.burden = 0
        return True

    def receive_grace(self, repented):
        """Grace is a gift, not earned by the code's logic."""
        if repented:
            print(f"[Grace] The state of '{self.state}' is being overwritten...")
            self.state = "Redeemed"
            self.has_faith = True
        else:
            print("[System] Repentance required to clear the burden.")

    def live_by_faith(self):
        if self.has_faith:
            return f"Status: {self.name} is walking in Faith."
        return f"Status: {self.name} is still searching."

# --- The Conversion Process ---
user = Soul("Seeker")

# 1. Recognizing the current state
print(f"Initial State: {user.state} (Burden: {user.burden})")

# 2. The act of turning (Metanoia)
has_turned = user.repent()

# 3. The transformation
user.receive_grace(has_turned)

# 4. The result
print(user.live_by_faith())
