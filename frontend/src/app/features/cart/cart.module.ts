import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CartRoutingModule } from './cart-routing.module';
import { CartComponent } from './pages/cart/cart.component';
import { CartItemComponent } from './components/cart-item/cart-item.component';
import { SharedModule } from '../../shared/shared.module';
import {FormsModule} from "@angular/forms";
import { CheckoutComponent } from './pages/checkout/checkout.component';

@NgModule({
  declarations: [CartComponent, CartItemComponent, CheckoutComponent],
  imports: [CommonModule, CartRoutingModule, SharedModule, FormsModule],
})
export class CartModule {}
