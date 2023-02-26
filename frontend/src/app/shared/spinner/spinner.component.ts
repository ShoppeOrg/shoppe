import { Component, OnInit } from '@angular/core';
import { SpinnerService } from '../services/spinner.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-spinner',
  templateUrl: './spinner.component.html',
  styleUrls: ['./spinner.component.scss']
})
export class SpinnerComponent implements OnInit {
  visibility$: Observable<boolean> | null = null;

  constructor(private spinnerService: SpinnerService) {}

  ngOnInit() {
    this.visibility$ = this.spinnerService.visibility$;
  }
}
