import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { StoryRoutingModule } from './story-routing.module';
import { StoryComponent } from './pages/story/story.component';

@NgModule({
  declarations: [StoryComponent],
  imports: [CommonModule, StoryRoutingModule]
})
export class StoryModule {}
