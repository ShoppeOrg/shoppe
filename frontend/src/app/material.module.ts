import { NgModule } from '@angular/core';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule, MatIconRegistry } from '@angular/material/icon';

@NgModule({
  imports: [MatIconModule, MatToolbarModule],
  exports: [MatIconModule, MatToolbarModule]
})
export class MaterialModule {
  constructor(iconRegistry: MatIconRegistry) {
    iconRegistry.setDefaultFontSetClass('material-icons-outlined');
  }
}
