# Cyberpunk — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Obsidian Base Canvas */
  --color-cyber-void: #060709;
  --color-cyber-bg: #0B0D13;
  --color-cyber-surface: #12151E;
  --color-cyber-surface-elevated: #1A1F2C;

  /* Neon High-Voltage Accents */
  --color-neon-cyan: #00F0FF;
  --color-neon-amber: #FFB800;
  --color-neon-magenta: #FF0055;
  --color-neon-green: #00FF66;

  /* HUD Lines & Dividers */
  --color-cyber-border: #1E2536;
  --color-cyber-border-active: #00F0FF;
  --color-cyber-grid: rgba(0, 240, 255, 0.06);

  /* Typography / Phosphor */
  --color-text-phosphor: #E8F4F8;
  --color-text-cyan: #00F0FF;
  --color-text-dim: #62728C;
  --color-text-muted: #3F4B5E;
}
```

## Border Radius & Chamfer Tokens

```css
:root {
  --radius-none: 0px; /* Sharp corners */
  /* Chamfer cut clip paths */
  --clip-chamfer-sm: polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 8px 100%, 0 calc(100% - 8px));
  --clip-chamfer-btn: polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 10px 100%, 0 calc(100% - 10px));
  --clip-notch-top: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%);
}
```

## Glow & Shadow Tokens

```css
:root {
  --glow-cyan-sm: 0 0 8px rgba(0, 240, 255, 0.4);
  --glow-cyan-lg: 0 0 20px rgba(0, 240, 255, 0.6), inset 0 0 10px rgba(0, 240, 255, 0.2);
  --glow-amber-sm: 0 0 8px rgba(255, 184, 0, 0.4);
  --glow-magenta-sm: 0 0 8px rgba(255, 0, 85, 0.4);
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px',
        none: '0px',
        sm: '0px',
        md: '0px',
        lg: '0px',
        full: '0px',
      },
      colors: {
        cyber: {
          void: '#060709',
          bg: '#0B0D13',
          surface: '#12151E',
          border: '#1E2536',
          cyan: '#00F0FF',
          amber: '#FFB800',
          magenta: '#FF0055',
          green: '#00FF66',
          phosphor: '#E8F4F8',
          dim: '#62728C',
        }
      },
      boxShadow: {
        'neon-cyan': '0 0 10px rgba(0, 240, 255, 0.4)',
        'neon-amber': '0 0 10px rgba(255, 184, 0, 0.4)',
        'neon-magenta': '0 0 10px rgba(255, 0, 85, 0.4)',
      }
    }
  }
}
```
