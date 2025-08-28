(() => {
    'use strict';

    const getStoredTheme = () => localStorage.getItem('theme');
    const setStoredTheme = theme => localStorage.setItem('theme', theme);

    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme();
        if (storedTheme) {
            return storedTheme;
        }
        return 'auto';
    }

    const applyTheme = theme => {
        const actualTheme = theme === 'auto'
            ? (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
            : theme;

        document.documentElement.setAttribute('data-bs-theme', actualTheme);
        document.body.classList.toggle('light-theme', actualTheme === 'light');
        document.body.classList.toggle('dark-theme', actualTheme === 'dark');
    }

    const showActiveTheme = (theme, focus = false) => {
        const themeSwitcher = document.querySelector('#bd-theme');
        if (!themeSwitcher) return;

        const themeSwitcherText = document.querySelector('#bd-theme-text');
        const activeThemeIcon = document.querySelector('.theme-icon-active');
        const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`);

        document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
            element.classList.remove('active');
            element.setAttribute('aria-pressed', 'false');
            element.querySelector('.fa-check').classList.add('d-none');
        });

        btnToActive.classList.add('active');
        btnToActive.setAttribute('aria-pressed', 'true');
        btnToActive.querySelector('.fa-check').classList.remove('d-none');

        activeThemeIcon.className = `fas ${btnToActive.querySelector('i').classList[1]} my-1 theme-icon-active`;
        themeSwitcher.setAttribute('aria-label', `${themeSwitcherText.textContent} (${theme})`);

        if (focus) {
            themeSwitcher.focus();
        }
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        const storedTheme = getStoredTheme();
        if (storedTheme !== 'light' && storedTheme !== 'dark') {
            const preferredTheme = getPreferredTheme();
            applyTheme(preferredTheme);
            showActiveTheme(preferredTheme);
        }
    });

    window.addEventListener('DOMContentLoaded', () => {
        const preferredTheme = getPreferredTheme();
        applyTheme(preferredTheme);
        showActiveTheme(preferredTheme);

        document.querySelectorAll('[data-bs-theme-value]').forEach(toggle => {
            toggle.addEventListener('click', () => {
                const theme = toggle.getAttribute('data-bs-theme-value');
                setStoredTheme(theme);
                applyTheme(theme);
                showActiveTheme(theme, true);
            });
        });
    });
})();
