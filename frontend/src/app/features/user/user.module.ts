import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserComponent } from './pages/user/user.component';
import { UserRoutingModule } from './user-routing.module';

@NgModule({
  declarations: [UserComponent],
  imports: [CommonModule, UserRoutingModule]
})
export class UserModule {}
