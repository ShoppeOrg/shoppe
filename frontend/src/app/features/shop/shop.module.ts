import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from 'src/app/material.module';
import { NgxStarRatingModule } from 'ngx-star-rating';
import { ShopRoutingModule } from './shop-routing.module';

import {ShopComponent} from './pages/shop/shop.component';
import { ShopItemComponent } from './components/shop-item/shop-item.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import {MatTabsModule} from '@angular/material/tabs';

@NgModule({
  declarations: [ShopComponent, ShopItemComponent],
  imports: [MaterialModule,
    CommonModule,
    ShopRoutingModule,
    NgxStarRatingModule,
    FormsModule,
    ReactiveFormsModule,
    MatTabsModule],
  providers: []
})
export class ShopModule {}
