
---

## **Mejiro McQueen Flirting Visual Novel Game**

### **Project Overview**

- This project is a **text-based interactive game** where players engage in conversations with the character **Mejiro McQueen**, building intimacy and uncovering unique storylines.  
- The dialogue system dynamically changes based on the character’s personality and situational context.  
- Player choices influence **affection levels**, triggering special events when certain conditions are met.

---

### **Key Features**

1. **Flirting System**
   - Player choices directly impact McQueen's affection levels.
   - Dialogue responses are tailored to McQueen’s personality traits (e.g., formal mode, casual mode, dessert preferences).
2. **Special Events**
   - Unlock exclusive events when specific affection thresholds or choices are met.
   - Special events provide deeper insights into McQueen's hidden personality.
3. **Diverse Choices**
   - Multiple dialogue options that reflect McQueen's character, such as formal conversation, interest-driven questions, or topics like desserts and sports.
   - Each choice creates a unique interaction.

---

### **Core Technologies and Tools**

- **Programming Language**: Python  
- **Libraries Used**: None (fully implemented from scratch)  
- **Key Features**:
  - Designed a class to manage game state and conversation history.  
  - Leveraged the `random` module to generate dynamic dialogues and randomize special events.  
  - Accessible text-based UI for simple and inclusive gameplay.

---

### **Code Structure**

1. **`MacqueenFlirtingGame` Class**
   - Manages the overall game logic and state.  
   - Handles character dialogue, affection calculations, and special event triggers.  
2. **Affection System**
   - The `calculate_affection_change` method adjusts affection levels based on player choices.  
3. **Dynamic Dialogue Generator**
   - Generates character responses that reflect McQueen’s personality and the current situation.  
4. **Special Events**
   - Trigger unique events when specific conditions are met.

---

### **How to Run the Game**

1. Run the game in a Python environment:  
   ```bash
   python macqueen_flirting_game.py
   ```  
2. Enter your player name → Choose dialogue options → Proceed with conversations → Discover unique endings.

---

### **Future Improvements**

1. **Adding a GUI**  
   - Incorporate visual elements using PyQt or Tkinter to create a richer user experience.  
2. **Expanding the Storyline**  
   - Introduce more scenarios, emotional depth, and branching dialogue paths.  
   - Add new characters and support multiplayer modes.  
3. **Web-Based Version**  
   - Transition the game to a web platform using Flask/Django.  
   - Share the game with a broader audience.  

---  
