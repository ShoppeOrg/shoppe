import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageHeaderComponent } from './page-header/page-header.component';
import { SpinnerComponent } from './spinner/spinner.component';
import { MaterialModule } from '../material.module';

@NgModule({
  declarations: [PageHeaderComponent, SpinnerComponent],
  imports: [CommonModule, MaterialModule],
  exports: [PageHeaderComponent, SpinnerComponent]
})
export class SharedModule {}
