import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { HeaderComponent } from './header/header.component';
import { MaterialModule } from '../material.module';
import { RouterModule } from '@angular/router';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './auth/pages/login/login.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { LoginFormComponent } from './auth/components/login-form/login-form.component';
import { AuthModalComponent } from './auth/modals/auth-modal/auth-modal.component';
import { SharedModule } from '../shared/shared.module';
import { CustomFormComponent } from './auth/shared/custom-form/custom-form.component';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule,
    RouterModule,
    ReactiveFormsModule,
    FormsModule,
    SharedModule
  ],
  declarations: [
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    NotFoundComponent,
    LoginFormComponent,
    AuthModalComponent,
    CustomFormComponent
  ],
  exports: [HeaderComponent, FooterComponent]
})
export class CoreModule {}
