import { createTheme } from '@mui/material';

const theme = createTheme({
    palette: {
        primary: {
            main: '#1E88E5',
        },
        secondary: {
            main: '#FFC107',
        },
    },
    typography: {
        primaryText: {
            color: '#FFFFFF',
        },
        secondaryText: {
            color: '#000000',
        },
    },
});

export default theme;
