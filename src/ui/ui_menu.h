#pragma once

#if defined(TARGET_STAX) || defined(TARGET_FLEX)
#define ICON_APP_HOME C_app_logo_64px
#elif defined(TARGET_APEX_P)
#define ICON_APP_HOME C_app_logo_48px
#endif

/**
 * Show main menu (ready screen, version, about, quit).
 */
void ui_menu_main(void);

#ifdef HAVE_BAGL
/**
 * Show settings submenu (blind signing toggle).
 */
void ui_menu_settings(void);
#endif

/**
 * Show about submenu (copyright, date).
 */
void ui_menu_about(void);
