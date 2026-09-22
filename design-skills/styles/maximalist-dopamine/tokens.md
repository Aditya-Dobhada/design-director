# Maximalist Dopamine — Design Tokens

## Color Tokens

```css
:root {
  /* High-Voltage Candy & Neon Palette */
  --color-dopamine-yellow: #FFF500;
  --color-dopamine-magenta: #FF007F;
  --color-dopamine-cyan: #00E5FF;
  --color-dopamine-lime: #00FF66;
  --color-dopamine-purple: #7A00FF;
  --color-dopamine-orange: #FF5E00;

  /* High-Contrast Bases */
  --color-canvas-black: #0D0D11;
  --color-canvas-candy-pink: #FFE5F1;
  --color-canvas-electric-cream: #FFFFE0;
  --color-ink-black: #000000;
  --color-ink-white: #FFFFFF;

  /* Card Surfaces */
  --color-card-surface-1: #FFF500;
  --color-card-surface-2: #FF007F;
  --color-card-surface-3: #00E5FF;
  --color-card-surface-white: #FFFFFF;
}
```

## Border & Offset Tokens

```css
:root {
  --border-dopamine-black: 3px solid #000000;
  --border-dopamine-heavy: 4px solid #000000;
  --border-dopamine-neon: 3px solid #00FF66;

  /* Colored Hard Offset Shadows (zero blur) */
  --shadow-dopamine-black: 5px 5px 0px #000000;
  --shadow-dopamine-magenta: 5px 5px 0px #FF007F;
  --shadow-dopamine-cyan: 5px 5px 0px #00E5FF;
  --shadow-dopamine-yellow: 5px 5px 0px #FFF500;
  --shadow-dopamine-double: 4px 4px 0px #FF007F, 8px 8px 0px #000000;
}
```

## Border Radius Tokens

```css
:root {
  --radius-chunky: 8px;
  --radius-pill: 9999px;
  --radius-sharp: 0px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderWidth: {
        DEFAULT: '3px',
        3: '3px',
        4: '4px',
      },
      boxShadow: {
        'dopamine-black': '5px 5px 0px #000000',
        'dopamine-magenta': '5px 5px 0px #FF007F',
        'dopamine-cyan': '5px 5px 0px #00E5FF',
        'dopamine-double': '4px 4px 0px #FF007F, 8px 8px 0px #000000',
      },
      colors: {
        dopamine: {
          yellow: '#FFF500', magenta: '#FF007F', cyan: '#00E5FF',
          lime: '#00FF66', purple: '#7A00FF', orange: '#FF5E00',
          candy: '#FFE5F1',
        }
      }
    }
  }
}
```
