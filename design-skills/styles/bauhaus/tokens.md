# Bauhaus — Design Tokens

## Color Tokens

```css
:root {
  /* Bauhaus Structural Canvas */
  --color-bauhaus-white: #FFFFFF;
  --color-bauhaus-black: #0A0A0A;    /* Near-black, functional */
  --color-bauhaus-gray: #E8E8E8;     /* Structural neutral */
  --color-bauhaus-gray-mid: #B0B0B0;

  /* The Primary Triad — ONLY these three accent colors */
  --color-bauhaus-red: #D62B2B;
  --color-bauhaus-yellow: #F5C800;
  --color-bauhaus-blue: #1B4FBD;

  /* Typography */
  --color-text-primary: #0A0A0A;
  --color-text-secondary: #3A3A3A;
  --color-text-muted: #707070;
  --color-text-on-dark: #FFFFFF;
  --color-text-on-primary: #FFFFFF;   /* For red/blue backgrounds */
  --color-text-on-yellow: #0A0A0A;   /* Black on yellow */
}
```

## Geometric Accent Tokens

```css
:root {
  /* Bauhaus circle accent size scales */
  --circle-sm: 16px;   /* Bullet / indicator */
  --circle-md: 48px;   /* Section accent */
  --circle-lg: 120px;  /* Hero accent medallion */
}
```

## Border & Structure Tokens

```css
:root {
  --border-structural: 2px solid #0A0A0A;
  --border-light: 1px solid #E8E8E8;
  --radius-none: 0px;          /* All rectangular elements */
  --radius-circle: 50%;        /* Bauhaus circle medallions */
  /* Any other radius value is FORBIDDEN */
}
```

## Shadow Tokens

```css
:root {
  --shadow-none: none; /* Drop shadows: FORBIDDEN */
  /* Depth = contrasting color planes only */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px', none: '0px', sm: '0px', md: '0px',
        lg: '0px', xl: '0px', full: '9999px', // full only for circles
      },
      boxShadow: { DEFAULT: 'none', none: 'none' },
      colors: {
        bauhaus: {
          black: '#0A0A0A', white: '#FFFFFF', gray: '#E8E8E8',
          red: '#D62B2B', yellow: '#F5C800', blue: '#1B4FBD',
        }
      }
    }
  }
}
```
